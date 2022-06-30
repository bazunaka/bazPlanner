using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Navigation;
using static bazPlannerWPF.sqlite_connect;
using static bazPlannerWPF.auth;
using static bazPlannerWPF.create_user;
using static bazPlannerWPF.create_project;
using static bazPlannerWPF.create_task;
using System.IO;

namespace bazPlannerWPF
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            DateTime now = DateTime.Now;
            Now_time.Content = now.ToString("D");
            
            if(sqlite_connect.Connect("test.db"))
            {
                Console.WriteLine("Connected!");
            }

            PresentMonth.SelectedDate = DateTime.Now;
            NextMonth.SelectedDate = DateTime.Now.AddMonths(+1);
            TwoNextMonth.SelectedDate = DateTime.Now.AddMonths(+2);

            //File.AppendAllText("log.txt", Environment.NewLine); логирование потом!
        }

        private void Connect_to_DB(object sender, RoutedEventArgs e)
        {
            if(CheckAuth() == 0)
            {
                create_user newUser = new create_user();
                newUser.Show();
            }
            
        }

        private void Create_project(object sender, RoutedEventArgs e)
        {
            create_project newProject = new create_project();
            newProject.Show();
        }

        private void Create_task(object sender, RoutedEventArgs e)
        {
            create_task newTask = new create_task();
            newTask.Show();
        }
    }
}
