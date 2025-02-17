using DocumentFormat.OpenXml.Packaging;
using DocumentFormat.OpenXml.Presentation;
using DocumentFormat.OpenXml.Drawing;
using DocumentFormat.OpenXml;
public class CreateSimplePPT
{

    public static void CreatePresentation(string filepath)
    {
        using (PresentationDocument presentationDocument = PresentationDocument.Create(filepath, DocumentFormat.OpenXml.PresentationDocumentType.Presentation))
        {
            // 创建演示文稿部分
            presentationDocument.AddPresentationPart();
            presentationDocument.PresentationPart.Presentation = new Presentation();

            // 创建幻灯片部分
            SlidePart slidePart = presentationDocument.PresentationPart.AddNewSlidePart();
            slidePart.Slide = new Slide(new CommonSlideData(new ShapeTree()));

            // 创建幻灯片ID列表
            presentationDocument.PresentationPart.Presentation.SlideIdList = new SlideIdList();
            uint slideId = 256; // Slide ID must be unique
            SlideId slideIdEntry = presentationDocument.PresentationPart.Presentation.SlideIdList.AppendChild(new SlideId() { Id = slideId, RelationshipId = presentationDocument.PresentationPart.GetIdOfPart(slidePart) });

            // 保存幻灯片
            slidePart.Slide.Save();
            presentationDocument.PresentationPart.Presentation.Save();
        }
    }


    public static void Main(string[] args)
    {
        string filepath = "SimplePresentation.pptx";
        CreatePresentation(filepath);
        System.Console.WriteLine($"PPT presentation created at {filepath}");
    }
}
