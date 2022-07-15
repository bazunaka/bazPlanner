using System.Windows;
using static bazPlannerWPF.Project;

namespace bazPlannerWPF
{
    public partial class create_project : Window
    {
        public create_project()
        {
            InitializeComponent();
        }

        private void AddProject(object sender, RoutedEventArgs e)
        {
            InsertProject(textNameProject.Text, "admin");
        }
    }
}
