using System.Windows;
using bazPlanner.Models;

namespace bazPlanner.Forms
{
    public partial class AddProject : Window
    {
        public AddProject()
        {
            InitializeComponent();
        }

        private void CreateNewProject(object sender, RoutedEventArgs e)
        {
            MainWindow? mainWindow = Application.Current.MainWindow as MainWindow;
            string nameUser = mainWindow.labelAuth.Content.ToString();
            Database.InsertProject(textNameProject.Text, nameUser);
            textNameProject.Clear();
        }
    }
}
