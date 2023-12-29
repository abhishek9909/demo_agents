using Microsoft.SemanticKernel;
using System.ComponentModel;

namespace CoreLogic.Plugins
{
    public class EmailPlugin
    {
        [KernelFunction]
        [Description("Sends an email to a recipient")]
        public async Task SendEmailAsync(Kernel kernel, [Description("Semicolon delimitated list of email of the recipients")] string recipients, string subject, string body)
        {
            // Logic to trigger emails.
            Console.WriteLine("Email sent");
        }

        [KernelFunction]
        [Description("Adds attachments in an email")]
        public async Task AddAttachment(Kernel kernel, [Description("Names of the files that the sender wants to send to the recipient")] string fileNames)
        {
            // Logic to add attachments.
            Console.WriteLine("Attachments added");
        }
    }
}
