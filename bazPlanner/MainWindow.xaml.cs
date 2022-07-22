using System;
using System.Windows;
using bazPlanner.Models;
using bazPlanner.Forms;

namespace bazPlanner
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            //Connect to database.
            Database.Connect();
            //Now time.
            DateTime now = DateTime.Now;
            labelTime.Content = now.ToString("D");

            Database.SelectTask();
        }

        //Show form for auth.
        private void FormAuth(object sender, RoutedEventArgs e)
        {
            Auth authWindow = new()
            {
                Owner = this
            };
            authWindow.Show();
        }

        private void AddProject(object sender, RoutedEventArgs e)
        {
            //Show form for add new project.
            AddProject addProject = new()
            {
                Owner = this
            };
            addProject.Show();
        }

        //Show name project if select item.
        private void listProjects_Selected(object sender, RoutedEventArgs e)
        {
            labelNameProject.Content = listProjects.SelectedItem.ToString();
            //Database.SelectTask(listProjects.SelectedItem.ToString());
        }

        private void AddTask(object sender, RoutedEventArgs e)
        {
            //Show form for add new task.
            AddTask addTask = new()
            {
                Owner = this
            };
            addTask.Show(); 
        }
    }
}
